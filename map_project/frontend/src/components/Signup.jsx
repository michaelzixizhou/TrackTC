import styled from 'styled-components';
import Select from "react-select";
import { useState } from "react";
import { useEffect } from 'react';

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
  let favAry = [];
  const [email, setemail] = useState('');
  const [fav, setfav] = useState('');
  const [ary, setary] = useState(null);

const handleSubmit = (e) => {
  e.preventDefault();
  const blog = {email, fav};
  console.log (blog);


  fetch ('http://127.0.0.1:8000/api/SignUp', {
    method: 'POST',
    headers: { "Content-Type": "application/json"},
    body: JSON.stringify(blog)
  }).then(function(response){
    console.log (blog);
    console.log ("Your setting have been saved. You will be notified whenever a problem occurs with the the selected lines.")
  })
  // .then(function(response){
  //   return response.json();
  // })
}

  const options = [
    { value: 'line1', label: 'Line 1' },
    { value: 'line2', label: 'Line 2' },
    { value: 'line3', label: 'Line 3' },
    { value: 'line4', label: 'Line 4' }
  ]

  useEffect(() => {
    if (ary != null){
      if (ary.length == 0){
        setfav(null);
      }
      else {
        setfav(ary[0].label);
        for (let i = 1; i < ary.length; i++){
          setfav(fav + "," + ary[i].label);
        }
      }
    }
  }, [ary]);

  for (let i = 1; i <= 999; i++){
    options.push({value: 'line' + i, label: 'Bus ' + i});
  }
 
  return (
    <SignUpWrapper> 
      <legend> Choose TTC and Bus lines you would like to receive emails:</legend><br/>
      <Select options={options} onChange={setary} width="2000px" defaultValue={ary} isMulti/><br/>{console.log(fav)}
      <form onSubmit={handleSubmit}>
        <input type="hidden" value={fav}/>
        <InputWrapper type="email" onChange={(e) => setemail(e.target.value)} placeholder="Your email address"/>
        <input type="submit" value="Submit"/>
      </form>
    </SignUpWrapper>
  );
}

export default Signup;