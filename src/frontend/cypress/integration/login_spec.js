describe('User Login', () => {
    it('should log in an existing user', () => {
      cy.visit('http://localhost:5001/login');
  
      cy.get('input[name="username"]').type('testuser');
      cy.get('form').submit();
  
      // Check if redirected to the profile page
      cy.url().should('include', '/profile');
      cy.contains('testuser');
    });
  });