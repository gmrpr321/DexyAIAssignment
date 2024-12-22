import { useState } from "react";
import Styles from "./MessageForm.module.css"
export default function MessageForm(props)
{
    const [isInfoHidden,setIsInfoHidden] = useState(true);
    const [appChoosen,setAppChoosen] = useState(1);
    const [recName,setRecName] = useState("");
    const [message,setMessage] = useState("");
   async function initiateRequest()
    {
        const payload = {appId : 0,recName :"",message : ""};
        payload.appId = appChoosen;
        payload.recName  = recName;
        payload.message = message; 
        console.log(payload);
        try{
            const res = await fetch("http://127.0.0.1:5000/api/sendMessage", {
                method: "POST",
                headers: {
                  "Content-Type": "application/json",
                },
                body: JSON.stringify(payload),
              });
        
              const result = await res.json();
              console.log(result);
            } catch (error) {
              console.error("Error:", error);
            }
        }
    return <div className={Styles.background}>
        <div className={Styles.appChooserow}>
            <button onClick={()=>{setAppChoosen(1);}}><img src="/wellfound.png" height={50} width={120} alt="No image found"
               className={appChoosen===1 ? Styles.chosenPlatform : Styles.notChosenPlatform}></img></button>
            <button onClick={()=>setAppChoosen(2)}><img src="/linkedin.png" height={50} width={120} alt="No image found" 
            className={appChoosen===2 ? Styles.chosenPlatform : Styles.notChosenPlatform}></img></button>
            <button 
            onClick={()=>setIsInfoHidden((value)=>!value)}>?</button>
        </div>
            <div className={Styles.recName}>
                <input onChange={(event)=>setRecName(event.target.value)} placeholder="Enter Recipient Name"></input>
            </div>
            <div className={Styles.message}>
                <input onChange={(event)=>setMessage(event.target.value)} placeholder="Enter Message"></input>
            </div>
            <div >
            <button onClick={()=>{initiateRequest()}} className={Styles.submitButton}>Send Message !</button>
        </div>
        <div className={isInfoHidden ?Styles.hideBox : Styles.showBox  }>
                <p>This uses Chrome Web Driver to automate the process, make sure it is installed in Your PC. (Click '?' to close)</p>
        
            </div>
        
    </div>
}