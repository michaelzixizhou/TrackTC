import { useEffect, useState } from "react";
import styled from 'styled-components';

const TableWrapper = styled.div`
  text-align: center;
  align-items: center;
  display: flex;
  gap: 4vw;
  margin: 20vh 10vw;
`;

const TitleLine1 = styled.span`
  text-decoration: solid;
  text-align: center;
  font-size: large;
  border-radius: 50px;
  padding: 10px;
  margin-bottom: 1vh;
  color: #fff;
  border-color: #fff;
  border-style: solid;
  background-color: #E64A19;
`;

const CustomTable = styled.table`
  display: flex;
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
                      <td><TitleLine1>Bus{post.busnumber}</TitleLine1></td>
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