
export const handleSearch = async (searchWord,setSearchResults) => {
    try {
      console.log('Searching')
      const response = await fetch('http://127.0.0.1:8000/search', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ searchWord }),
      });
      const data = await response.json();
      setSearchResults(data);
    
    } catch (error) {
      console.error(error);
    }
  };