import axios from 'axios'
import { useEffect } from 'react'
export default function Home() {
  const FetchData = async ()=> {
    console.log("HO")
    const res = await axios.get('http://127.0.0.1:5000/helloWorld')
    console.log(res)
  }
  useEffect(()=>{
    FetchData()
  },[])
  return (
    <div>
      <p>Home</p>
        <img src="http://127.0.0.1:5000/video_feed" alt=""/>
    </div>
  )
}
