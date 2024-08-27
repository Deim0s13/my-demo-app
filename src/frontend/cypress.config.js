const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    baseUrl: 'http://localhost:5001',  // Ensure this matches your Flask server's URL
    setupNodeEvents(on, config) {
      // implement node event listeners here if needed
    },
  },
});