import { useState } from 'react';
import Data from "./Data.js";
const Guns = () => { 
    //let image = " "
    const [image,setImage] = useState('')
    const [width, setWidth] = useState() 
    const [datas, setDatas] = useState([
        { image: '"M200-tan.webp"', name: 'CheyTac M200 Intervention', desription: '',width:650, id:1 },
        { image: 'ar-15.png', name: 'AR-15', desription:'',width:570, id:2},
        { image: 'machine gun.png', name: 'CheyTac M200 Intervention', desription:'',width:610,id:3}
    ])
    const clickButtonSniper = () => {
        setImage("M200-tan.webp") 
        setWidth(650)
    }
    const clickButtonAR_15 = () => {
        setImage("ar-15.png")
        setWidth(570)
    }
    const clickButtonMachineGun = () => {
        setImage("machine gun.png")
        setWidth(610)
    }
    return (
        <div className="Guns">  
           

            <div className="All-guns">
                <ul>
                    <li>
                        <button onClick={clickButtonSniper }>
                            SNIPER
                        </button>
                    </li>
                    <li>
                        <button onClick={clickButtonAR_15}>
                           AR-15
                        </button>
                    </li>
                    <li>
                        <button onClick={clickButtonMachineGun}>
                            MACHINE GUN
                        </button>
                    </li>
                </ul>
            </div>
            <div className="Gun-box-2" >
               
                <div className="Gun-image-box">
                    <img src={image} width={width }  />
                   
                </div>

               
                <Data datas={ datas } />
                
            </div>
        </div>
    )
} 
export default Guns;