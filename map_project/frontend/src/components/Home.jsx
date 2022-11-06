import Table from "./Table.jsx";
import Title from "./subcomponent/Title.jsx";
import Subtitle from "./subcomponent/Subtitle.jsx";
import styled from 'styled-components';

const HomeWrapper = styled.div`
  margin: min(20rem, 30vh) 0;
`;

const RedText = styled.span`
  color: #8B0000;
`;

const GreenText = styled.span`
  color: #006400;
`;

const GoldText = styled.span`
  color: #8B4513;
`;

const Home = () => {
  return (
    <HomeWrapper>
      <Title><RedText>Alert</RedText> yourself on potential <GreenText>TTC</GreenText>/<GoldText>Bus</GoldText> accidents.</Title>
      <Subtitle>TrackTC will take care of all accidents in Downtown Toronto along your commute, using reliable database system.</Subtitle>
      <Table/>
    </HomeWrapper>
  );
}

export default Home;