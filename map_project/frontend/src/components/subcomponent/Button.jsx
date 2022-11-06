import styled from 'styled-components';

const InputWrapper = styled.input`
  /* Adapt the colors based on primary prop */
  background: #fff;
  color: #000;
  font-size: 1em;
  margin: 1em;
  padding: 0.25em 1em;
  border: 2px solid #000;
  border-radius: 4px;
`;

const Input = (props) => {
  return (
    <>
      <InputWrapper type="text" placeholder="Your email address"/>
      <InputWrapper type="submit" placeholder="Receive Alerts"/>
    </>
  );
}

export default Input;