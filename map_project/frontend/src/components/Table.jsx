import { useEffect, useState } from "react";
import styled from 'styled-components';

const TableWrapper = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1vw;
  margin: 20vh 0;
`;

const TitleLine1 = styled.div`
  text-decoration: solid;
  text-align: center;
  padding: min(1.5vw, 0.5rem);
  color: #fff;
  width: 2rem;
  height: 2rem;
  border-color: #fff;
  border-style: solid;
  border-radius: 100px;
  background-color: #E64A19;
`;

const Line = styled.p`
  vertical-align: center;
  font-size: min(3vw, 1rem);
  bottom: 10px;
  position: relative;
`;

const CustomTable = styled.table`
  display: flex;
  background: white;
  width: min(80vw, 50rem);
  border-radius: 20px;
  overflow-wrap: anywhere;
`;

const Table = () => {
  const [posts, setPosts] = useState([]);
  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/BusAlert')
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
          setPosts(data);
        })
        .catch((err) => {
          console.log(err.message);
        });
  }, []);

  return (
    <TableWrapper>
      {posts.map((post) => {
          return (
          <CustomTable>
              <thead>
                  <tr>
                      <td><TitleLine1><Line>{post.busnumber}</Line></TitleLine1></td>
                  </tr>
              </thead>
              <tfoot>
                  <tr><td>{post.busname}</td></tr>
                  <tr><td>{post.delaymessage}</td></tr>
              </tfoot>
          </CustomTable>);
      })}
    </TableWrapper>
  );
}

export default Table;