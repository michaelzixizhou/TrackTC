import styled from 'styled-components';

const SubtitleWrapper = styled.h2`
  font-size: 24px;
  line-height: 34px;

  text-align: center;
  margin: 0 5vw;
  color: rgba(0, 0, 0, 0.8);
`;

const Subtitle = (props) => {
  return (
    <SubtitleWrapper>
      {props.children}
    </SubtitleWrapper>
  );
}

export default Subtitle;