import { useState } from 'react';

const Mw2 = () => {
    const [chars, setchars] = useState([
        { Nickname: 'SOAP', Name: 'JOHN MACTAVISH ', Team: 'BRAVO TEAM', Nationality: 'BRITISH', Rank: 'CAPTAIN', Relationship: 'TASK FORCE 141', Image: '', id:1},
        { Nickname: 'BLACKVIKING', Name: 'JOHN MACTAVISH ', Team: 'BRAVO TEAM', Nationality: 'BRITISH', Rank: 'CAPTAIN', Relationship: 'TASK FORCE 141', Image: '', id:2},
        { Nickname: 'GHOST', Name: 'JOHN MACTAVISH ', Team: 'BRAVO TEAM', Nationality: 'BRITISH', Rank: 'CAPTAIN', Relationship: 'TASK FORCE 141', Image: '',id:3},
    ]);
    return ( 
        <div className="Mw2"> 
            <div className="Players">
                <h1>MORDERN WARFARE 2</h1>
                <div className="Player-image">
                    <img />
                </div> 
                <div className="Player-text"> 
                    <h2>Nickname</h2>
                    <p>Name</p>
                    <p className="Input">Name input</p> 
                    <p>Name input</p> 
                    <p className="Input">Name input</p> 
                    <p>Name input</p> 
                    <p className="Input">Name input</p> 
                    <p>Name input</p> 
                    <p className="Input">Name input</p>  
                </div>
            </div>
            
        </div>
        
    )
} 
export default Mw2;