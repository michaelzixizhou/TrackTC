import { useState } from "react";
import styled from 'styled-components';

const BusList = styled.span`
  color: #fff;
  text-decoration: none;
  transition: all 0.1s ease-out;
  margin-right: 25vw;
  margin-top: 1.5rem;
  text-align: center;
  background-color: red;
`;

const TitleLine1 = styled.h2`

  text-decoration: solid;
  text-align: center;
  font-size: large;
  border-radius: 50px;
  color: #000000;
  background-color: #bdcf22;
`;



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
              <span>
                {keys.map((key) => {
                    return (
                    <table>
                        <thead>
                            <tr>
                                <TitleLine1>{key}</TitleLine1>
                            </tr>
                        </thead>
                        
                           <BusList> {getAccidents(Info[key])} </BusList>
                        
                    </table>);
                })}
            </span>

  );
}

export default Table;