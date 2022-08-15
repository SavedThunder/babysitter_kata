import React, {useState} from 'react';
import { TimePicker, Button, Checkbox } from 'antd';
import moment from 'moment';


function NightlyForm() {

    const [bedtimeFlag, setBedtimeFlag] = useState(true)
    const [startTime, setStartTime] = useState()
    const [endTime, setEndTime] = useState()
    const [bedTime, setBedTime] = useState()
    const [charge, setCharge] = useState('')
    const [disabledTime, setDisabledTime] = useState([5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
    const [disabledEnd, setDisabledEnd] = useState(disabledTime)
    const [disabledBed, setDisabledBed] = useState(disabledTime)

    const changeStart = (time, timeString) => {
        setStartTime(timeString)
        console.log(time)
        console.log(timeString)
    };
    
    const changeEnd = (time, timeString) => {
        setEndTime(timeString)
    }
    
    const changeBed = (time, timeString) => {
        setBedTime(timeString)
    }

    const toggleBedtime = () => {
        if(bedtimeFlag){
            setBedtimeFlag(false);
        }
        else{
            setBedtimeFlag(true);
        }
    }
    
    const calculateEndpoint = async () => {
        const response = await fetch('http://localhost:5000/calculate_balance', {
            method: 'POST',
            body: JSON.stringify({
                'start_time':startTime,
                'end_time': endTime,
                'bed_time': bedTime
            }),
            headers: {
                'Content-Type' : 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        });
        const nightly_charge = await response.json();
        setCharge(nightly_charge)
    }

    return (
        <>
            <h3>Nightly Charge Form</h3>
            <TimePicker 
                format="HH:mm"
                onChange={changeStart}

            />
            <TimePicker 
                format="HH:mm"
                onChange={changeEnd}
            />
            <Checkbox 
                onChange={toggleBedtime}
                defaultChecked={bedtimeFlag}>
                Bedtime?
            </Checkbox>

            <TimePicker 
                format="HH:mm"
                onChange={changeBed}
                disabled={!bedtimeFlag}
            />
            <Button disabled={startTime ? endTime ? false : true : true}
                    onClick={calculateEndpoint}>Calculate
            </Button>

            <p>{charge}</p>
        </>

    )
}

export default NightlyForm