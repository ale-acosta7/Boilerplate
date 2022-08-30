const path = require('path');
const webpack = require('webpack');

const paths = {
    DIST: path.resolve(__dirname, './static/dist'),
    SRC: path.resolve(__dirname, './src'),
    TEMPLATES: path.resolve(__dirname, './templates')
};

module.exports = {
    entry: path.join(paths.SRC, 'index.tsx'),
    devtool: 'inline-source-map',
    module: {
        rules: [
            {
                test: /\.tsx?$/,
                exclude: /node_modules/,
                use: 'babel-loader'
            },
            {
                test: /\.css$/i,
                use: ['style-loader', 'css-loader']
            }
        ]
    },
    resolve: {
        extensions: ['.tsx', '.ts', '.js']
    },
    output: {
        path: paths.DIST,
        filename: '[name].js'
    },
    plugins: [
        new webpack.DefinePlugin({
            'process.env.NODE_ENV': JSON.stringify('development')
        }),
        new webpack.DefinePlugin({
            process: 'process/browser'
        })
    ]
};