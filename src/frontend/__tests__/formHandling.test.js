// Example of a simple login function
function login(username) {
    return username === "admin" ? "Welcome, admin!" : "Login failed";
  }
  
  test('login with correct username', () => {
    const result = login('admin');
    expect(result).toBe('Welcome, admin!');
  });
  
  test('login with incorrect username', () => {
    const result = login('guest');
    expect(result).toBe('Login failed');
  });