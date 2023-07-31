const VehiclesList = (props) => {
    const vehicles = props.vehicles
    return (
        <div className="Vehicles" id='New'>
            {vehicles.map((vehicle) => (


                <div className="New-gun">
                    <img src={vehicle.image} width={vehicle.width} />
                    <h2>{vehicle.name}</h2>
                </div>


            ))}
        </div>
    )
}
export default VehiclesList;