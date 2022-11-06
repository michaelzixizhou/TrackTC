import styled from 'styled-components';

const TitleWrapper = styled.h1`
  font-size: min(10vw, 5rem);
  line-height: 110%;

  text-align: center;
  letter-spacing: -0.04em;
  color: #000000;
  text-shadow: 0px 4px 4px #777;
`;

const Title = (props) => {
  return (
    <TitleWrapper>
      {props.children}
    </TitleWrapper>
  );
}

export default Title;