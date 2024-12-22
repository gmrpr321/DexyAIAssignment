import Styles from "./Header.module.css"
export default function Header(props)
{
return<div className={Styles.header}>
    <div className={Styles.headTextContent}>
        <p>Message Automation Tool</p>
        </div>    
        <div className={Styles.subTextContent}>
            <p>Use this tool to automate the process of sending messages on your favourite platform !</p>
        </div>
</div>    
}