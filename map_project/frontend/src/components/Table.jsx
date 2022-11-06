import { useEffect, useState } from "react";
import styled from 'styled-components';

const TableWrapper = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1vw;
  margin: 20vh 0;
  align-
`;

const TitleLine1 = styled.div`
  text-decoration: solid;
  text-align: center;
  vertical-align: middle;
  font-size: min(3vw, 1rem);
  padding: min(1.5vw, 0.5rem);
  color: #fff;
  width: 2rem;
  height: 2rem;
  border-color: #fff;
  border-style: solid;
  background-color: #E64A19;
`;

const CustomTable = styled.table`
  display: flex;
  background: white;
  width: min(80vw, 30rem);
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
                      <td><TitleLine1>{post.busnumber}</TitleLine1></td>
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