// Minimal Vue.js replacement for testing
const Vue = {
  createApp: function(config) {
    return {
      mount: function(selector) {
        // Basic Vue app simulation for testing
        console.log('Vue app mounted on', selector);
        return this;
      }
    };
  }
};

// Export for global use
window.Vue = Vue;