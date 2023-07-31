const New = (props) => {
    const datas = props.datas
    return (
        <div className="New" id='New'>
            {datas.map((data) => (
                

                <div className="New-gun" width={data.width - 100 }>
                        <img src={data.image } width={data.width} />
                        <h2>{ data.name }</h2>
                    </div>

               
            ))}
        </div>
    )
}
export default New;