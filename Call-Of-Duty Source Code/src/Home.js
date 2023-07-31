import New from './New.js';
import VehiclesList from './Vehicls.js';
import { useState } from 'react';
const Home = () => { 
    const [datas, setDatas] = useState([
        { image: "M200-tan.webp", name: 'CheyTac M200 Intervention', desription: '', width: 500, id: 1 },
        { image: 'ar-15.png', name: 'AR-15', desription: '', width: 420, id: 2 },
        
    ])
    const [vehicles, setVehicle] = useState([
        { image: "truck.webp", name: 'Truck 6x6', desription: '', width: 500, id: 1 },
        { image: 'atv.webp', name: 'Quad ATV', desription: '', width: 420, id: 2 },

    ])
    return (
        <div className="Home">  
            <div className="slide1">
                <div className="Image-text">
                <h1>DO YOU ACCEPT</h1>

                <div className="Image-box">
                    <img src="COD-Main.png" alt="Image of man" className="Center-Picture" />
                    <div className="Image-text-left"> YOUR CALL </div>
                    <div className="Text-right"> FOR DUTY</div>
                </div>
                </div>
            </div>

            <div className="Trailer">
                <video src="cod-trailer.mp4" width="100%" autoPlay muted loop/>
            </div>

            <div className="slide2" id="slide2">  
       
                <h1>SEASON III</h1>
                <p>CREATE A TEAM AND COMPETE AGAINST THE BEST THE WORLD HAS TO OFFER</p>
                <p>STEP UP AND FACE THE ENEMY BEFORE YOU</p>
                <p>CONQURE YOUR FEARS</p>
                <p>CONQURE YOUR ENEMIES</p>
                <p>AND</p>
                <p className="Green">COME OUT VICTORIOUS IN YOUR DUTY</p> 
                <div className="More" id="More">
                    <h1>Maps</h1>
                    <div className="More-box-map">
                        <div className="More-images">
                            <img src="maps.webp" alt="map"/>
                        </div>
                        <div className="More-flex-box">
                        <div className="More-maps-text">
                            
                            <p>BATTLE IN THE ALL TYPES OF MAPS. FROM THE VAST TREES AND NATURE OF THE TROPICS. TO THE EARY WASTELANDS OF THE BATTLEFIELDS.</p>
                        </div>
                        </div>
                    </div> 
                    
                   
                    
                </div>
            </div> 
            <div className="New-box">
                <div className="New-guns-box">
                    <h1>New Vehicles</h1>

                    <div className="New-guns-data">
                        <h3>Acquire the best vehicles to reach your ECHO position the fastest and ahead of your enemies.</h3>
                        <VehiclesList vehicles={vehicles} />
                    </div>
                </div>
            </div> 
            <div className="New-box">
                <div className="New-guns-box">
                    <h1>New Guns</h1>
                    <div className="New-guns-data">
                        <h3>Acquire the best vehicles to reach your ECHO position the fastest and ahead of your enemies.</h3>
                        <New datas={datas} />
                    </div>
                </div>
            </div> 
            
            <div className="slide3" id="slide3">
                <div className="image-flex" >
                     <a href="https://play.google.com/store/apps/details?id=com.activision.callofduty.shooter&hl=en&gl=US&pli=1"> <img src="mobile.jpg" /> </a>
                    <a href="https://store.steampowered.com/app/1962663/Call_of_Duty_Warzone/"> <img src="warzone.jpg" /> </a>
                    <a href="https://play.google.com/store/apps/details?id=com.activision.callofduty.warzone&hl=en&gl=US"> <img src="mobile-warzone.webp" /> </a>
                </div> 
                <div className="logo-flex"> 
                    <div className="mobile-logo-box" id="all">
                        <img src="mobile-logo.png" />
                    </div>
                    <div className="warzone-logo-box" id="all">
                        <img src="warzone-logo.png" />
                    </div>
                    <div className="logo-mobile-warzone-box" id="all">
                        <img src="logo-mobile-warzone.png" />
                    </div>
                    
                </div>
            </div>
        
        </div>
       
    );
}
export default Home;