import Table from "./Table.jsx";
import Title from "./subcomponent/Title.jsx";
import Subtitle from "./subcomponent/Subtitle.jsx";
import Input from "./subcomponent/Button.jsx";
import styled from 'styled-components';

const HomeWrapper = styled.div`
  margin: min(20rem, 30vh) 0;
  /* background-image: linear-gradient(to bottom, rgb(96, 114, 179), rgb(145, 95, 149)); */

`;

// const RedText = styled.span`
//   color: #8B0000;
// `;

const whiteText = styled.span`
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
      <Title><GoldText>Alert yourself on potential <whiteText>TTC</whiteText> Bus accidents.</GoldText></Title>
      <Subtitle>TrackTC will take care of all accidents in Downtown Toronto along your commute, using reliable database system.</Subtitle>
      {/* <Input>Enter your email address</Input> */}
      <Table/>
    </HomeWrapper>
  );
}

export default Home;