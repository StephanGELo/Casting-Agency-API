import React, { useState, useEffect } from 'react';

export const useDataFetching = (url, initialData, token, body) => {
    const [data, setData] = useState(initialData)

    useEffect(() => {
        async function retrieveData() {
            const response = await fetch(url, {
                method: 'GET',
                headers: {
                    Authorization: `Bearer ${token}`,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(body)
            })
            setData(await response.json())
        }
        retrieveData()
    }, [url, token])
    
    return data;
}