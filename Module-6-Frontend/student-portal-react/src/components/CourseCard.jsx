// import React from 'react';

const CourseCard = (props) => {
          return (
                    (props.isEnrolled===false) 
                    ?
                    <div style={cardStyle}>
                              <h3 style={{ margin: '0 0 10px 0' }}>{props.name}</h3>
                              <p><strong>Code:</strong> {props.code}</p>
                              <p><strong>Credits:</strong> {props.credits}</p>
                              <p><strong>Grade:</strong> <span>{props.grade}</span></p>
                              <button onClick={props.onEnroll}>Enrol</button>
                    </div>
                    
                    :
          
                    <div style={card1Style}>
                              <h3 style={{ margin: '0 0 10px 0' }}>{props.name}</h3>
                              <p><strong>Code:</strong> {props.code}</p>
                              <p><strong>Credits:</strong> {props.credits}</p>
                              <p><strong>Grade:</strong> <span>{props.grade}</span></p>
                    </div>
          
          
          );
}
const cardStyle = {
          border: '1px solid #ddd',
          margin: '2%',
          minWidth: '250px',
};
const card1Style = {
          border: '1px solid #ddd',
          margin: '2%',
          minWidth: '250px',
          backgroundColor:'lightgreen'
};


export default CourseCard;