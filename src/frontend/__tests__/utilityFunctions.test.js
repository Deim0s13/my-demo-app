// Example utility function
function formatUsername(username) {
    return username.trim().toLowerCase();
  }
  
  test('formats username correctly', () => {
    const result = formatUsername('  Admin  ');
    expect(result).toBe('admin');
  });