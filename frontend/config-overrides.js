const { override } = require('customize-cra');
const CspHtmlWebpackPlugin = require("@melloware/csp-webpack-plugin");

const cspConfigPolicy = {
    'default-src': "'none'",
    'object-src': "'none'",
    'base-uri': "'self'",
    'connect-src': "'self' 'unsafe-inline' 'unsafe-eval' ws:",
    'worker-src': "'self'",
    'img-src': "'self' blob: data: content:",
    'font-src': "'self'",
    'frame-src': "'self'",
    'manifest-src': "'self'",
    'script-src': ["'unsafe-inline'", "'self'", "'unsafe-eval'"],
};

function addCspHtmlWebpackPlugin(config) {
    config.plugins.push(new CspHtmlWebpackPlugin(cspConfigPolicy, {
        enabled: true,
        integrityEnabled: false,
        primeReactEnabled: false,
        trustedTypesEnabled: false,
        hashingMethod: 'sha384',
        hashEnabled: {
            'script-src': false,
            'style-src': false
        },
        nonceEnabled: {
            'script-src': false,
            'style-src': false
        },
    }));
    config.output.crossOriginLoading = "anonymous";
    return config;
}

module.exports = {
    webpack: override(addCspHtmlWebpackPlugin),
};