import Table from "./Table.jsx";
import Title from "./subcomponent/Title.jsx";
import Subtitle from "./subcomponent/Subtitle.jsx";
import styled from 'styled-components';

const HomeWrapper = styled.div`
  margin: min(20rem, 30vh) 0;
  /* background-image: linear-gradient(to bottom, rgb(96, 114, 179), rgb(145, 95, 149)); */

`;

// const RedText = styled.span`
//   color: #8B0000;
// `;

const WhiteText = styled.span`
  color: #eff8ef;
`;

const GoldText = styled.span`
  color: #f0de18;
`;

const TitleLine1 = styled.span`
  text-decoration: solid;
  text-align: center;
  font-size: large;
  border-radius: 50px;
  color: #000000;
  background-color: #bdcf22;
`;

const Home = () => {
  return (
    <HomeWrapper>
      <Title><GoldText>Notify yourself on potential <WhiteText>TTC</WhiteText>/Bus alerts.</GoldText></Title>
      <Subtitle>TrackTC will take care of all TTC alerts in Downtown Toronto along your commute, using reliable database system.</Subtitle>
      <Table/>
    </HomeWrapper>
  );
}

export default Home;