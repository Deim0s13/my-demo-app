describe('User Registration', () => {
    it('should register a new user', () => {
      cy.visit('http://localhost:5001/register');
  
      cy.get('input[name="username"]').type('testuser');
      cy.get('input[name="email"]').type('test@example.com');
      cy.get('form').submit();
  
      // Check if redirected to the profile page
      cy.url().should('include', '/profile');
      cy.contains('testuser');
      cy.contains('test@example.com');
    });
  });