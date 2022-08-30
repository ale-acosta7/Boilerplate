import logging
import multiprocessing as mp
import threading
import sys
import traceback
import socket
import queue

class MultiProcessingHandler(logging.Handler):
    def __init__(self, name: str = '', sub_handler = None):
        super(MultiProcessingHandler, self).__init__()
        if sub_handler is None:
            sub_handler = logging.StreamHandler()
        self.sub_handler = sub_handler

        self.setLevel(self.sub_handler.level)
        self.setFormatter(self.sub_handler.formatter)
        self.filters = self.sub_handler.filters

        self.queue = mp.Queue(-1)
        self._is_closed = False
        # Thread handles receiving records asynchronously
        self._receive_thread = threading.Thread(target=self._receive, name=name)
        self._receive_thread.daemon = True
        self._receive_thread.start()

    def setFormatter(self, fmt):
        super(MultiProcessingHandler, self).setFormatter(fmt)
        self.sub_handler.setFormatter(fmt)

    def _receive(self):
        try:
            broken_pipe_error = BrokenPipeError
        except NameError:
            broken_pipe_error = socket.error
        while True:
            try:
                if self._is_closed and self.queue.empty():
                    break
                record = self.queue.get(timeout=0.2)
                self.sub_handler.emit(record)
            except (KeyboardInterrupt, SystemExit):
                raise
            except (broken_pipe_error, EOFError):
                break
            except queue.Empty:
                pass # This periodically checks if the logger is closed
            except:
                traceback.print_exc(file=sys.stderr)
        self.queue.close()
        self.queue.join_thread()

    def _send(self, s):
        self.queue.put_nowait(s)
    
    def _format_record(self, record):
        # Ensure that exc_info and args
        # have been stringified. Removes any chance of
        # unpickable things inside and possible reduces
        # message size sent over pipe.
        if record.args:
            record.msg = record.msg % record.args
            record.args = None

        if record.exc_info:
            self.format(record)
            record.exc_info = None

        return record

    def emit(self, record):
        try:
            s = self._format_record(record)
            self._send(s)
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)

    def close(self):
        if not self._is_closed:
            self._is_closed = True
            self._receive_thread.join(5.0) # Waits for receive queue to empty.

            self.sub_handler.close()
            super(MultiProcessingHandler, self).close()