/**
 * vue.config.js
 *
 * See: https://cli.vuejs.org/config/#configuration-reference
 */
module.exports = {
    devServer: {
        proxy: {
            '/api/*': {
                target: 'http://localhost:5000'
            }
        }
    }
};

