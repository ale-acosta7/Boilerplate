import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Test from "./components/test";

const App: React.FC = () => {
    return (
        <Router>
            <Routes>
                <Route path='/' element={<Test/>}/>
            </Routes>
        </Router>
    );
}

const root = ReactDOM.createRoot(
    document.getElementById('app') as HTMLElement
);

root.render(<App/>);