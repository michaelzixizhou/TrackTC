const Table = () => {
    const Info = {
      "Line 1": [
          "Queen's Park- Street Car Blocked", 
          "Road Blocked at St.George", 
      ],
      "Bus": [
          "Bus Line 25 is over", 
          "Bus Line 19 is over", 
          "Bus Line qr83q is over", 
          "Bus Line is over", 
          "Bus Line is over", 
          "Bus Line is over"
      ],
      "Bus2": [
          "Bus Line 25 is over", 
          "Bus Line 19 is over", 
          "Bus Line qr83q is over", 
          "Bus Line is over", 
          "Bus Line is over", 
          "Bus Line is over"
      ],
  };

  const keys = Object.keys(Info);

  const getAccidents = (arr) => {
    return arr.map((accident) => (
      <tr><td>{accident}</td></tr>
    ));
  }

  return (
      <details>
          <summary>Accidents</summary>
          <span>
              <span>
                {keys.map((key) => {
                    return (
                    <table>
                        <thead>
                            <tr>
                                <th>{key}</th>
                            </tr>
                        </thead>
                        <tbody>
                            {getAccidents(Info[key])}
                        </tbody>
                    </table>);
                })}
              </span>
          </span>
      </details>
  );
}

export default Table;