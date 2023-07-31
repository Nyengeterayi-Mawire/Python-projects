const DataList = (props) => { 
    const datas= props.datas
    return (
        <div className="DataList"> 
            {datas.map((data) => (

                <div className="Info">                   
                    <h2>{data.name}</h2>
                    <ul className="Info-bullets">
                        <li>{data.bullet_1}</li>
                        <li>{data.bullet_2} </li>
                        <li>{data.bullet_3} </li>
                        <li>{data.bullet_1}</li>
                    </ul>
                </div>
            ))}
        </div>
    )
} 
export default DataList;