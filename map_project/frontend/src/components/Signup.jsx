import styled from 'styled-components';
import Select from "react-select";

const SignUpWrapper = styled.div`
  margin: min(20rem, 30vh) 0;
  display: flex;
  flex-direction: column;
  align-items: center;
`;

const InputWrapper = styled.input`
  background: #fff;
  color: #000;
  font-size: 1em;
  margin: 1em;
  padding: 0.25em 1em;
  border: 2px solid #000;
  border-radius: 4px;
`;

const Signup = () => {
  const options = [
    { value: 'line1', label: 'Line 1' },
    { value: 'line2', label: 'Line 2' },
    { value: 'line3', label: 'Line 3' },
    { value: 'line4', label: 'Line 4' }
  ]

  for (let i = 1; i <= 999; i++){
    options.push({value: 'line' + i, label: 'Bus ' + i});
  }

  return (
    <SignUpWrapper> 
      <legend>Choose TTC and Bus lines you would like to receive emails:</legend>
      <Select options={options} width="2000px" isMulti/>
      <InputWrapper type="text" placeholder="Your email address"/>
      <InputWrapper type="submit" value="Submit"/>
    </SignUpWrapper>
  );
}

export default Signup;