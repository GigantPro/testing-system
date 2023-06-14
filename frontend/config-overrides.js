const { override } = require('customize-cra');
const CspHtmlWebpackPlugin = require("@melloware/csp-webpack-plugin");

const cspConfigPolicy = {
    'default-src': "'self' data: content: blob:",
    'object-src': "blob:",
    'base-uri': "'self'",
    'connect-src': "'self'",
    'worker-src': "'self'",
    'img-src': "'self' blob: data: content:",
    'font-src': "'self'",
    'frame-src': "'self'",
    'manifest-src': "'self'",
    'style-src': ["'self'"],
    'script-src': ["'strict-dynamic'"]
};

function addCspHtmlWebpackPlugin(config) {
    if (process.env.NODE_ENV === 'production') {
        config.plugins.push(new CspHtmlWebpackPlugin(cspConfigPolicy));
        config.output.crossOriginLoading = "anonymous";
    }
    return config;
}

//module.exports = {
//    webpack: override(addCspHtmlWebpackPlugin),
//};
