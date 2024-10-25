import React from 'react';
import '../App.css'; 

function Hello(props) {
  const someStyle = {backgroundColor:"black", color:"white"};
  return(
    <div>
      <h1 style={someStyle}>안녕, {props.name} 1호</h1>
      <h1>안녕, {props.name} 2호!</h1>
      <div className="newClass"/>
    </div>
  )
}

export default Hello;