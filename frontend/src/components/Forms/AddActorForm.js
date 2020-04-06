import { API_URL } from '../../utils/auth_config';
import React, { useState } from 'react';
import { NavLink as RouterNavLink } from 'react-router-dom';
import { 
    Card,
    CardHeader,
    CardBody,
    CardFooter,
    Button,
    Form,
    FormGroup,
    Label,
    Input,
    FormText
 } from 'reactstrap';


export const AddActorForm = props => {
    const url = `${API_URL}/actors`;
    const { editing, actor, token } = props.location.state;
    const [ actorInput, setActorInput ] = useState({
        name: (editing && actor && actor.name) || "",
        age: (editing && actor && actor.age) || "",
        gender: (editing && actor && actor.gender) || "",
        movie: (editing && actor && actor.movie) || ""
    });

    const updateFormFields = (field, value) => {
        setActorInput({
            ...actorInput,
            [field]: value
        })
    };

    const handleFormSubmit = async (id, data) => {
        const result = await fetch(editing ? `${url}/${id}` : url, {
            method: editing ? "PATCH" : "POST",
            headers: {
                Authorization: `Bearer ${token}`,
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const response = await result.json();

        setActorInput({
            name: response.added_actor.name,
            age: response.added_actor.age,
            gender: response.added_actor.gender,
            movie:response.added_actor.movie
        });
        props.history.push('/actors-details')
    };


    return (
        <Card inverse style={{ backgroundColor:'#333', borderColor:'#333'}}>
            <CardHeader className="text-primary" style={{fontSize:14}}>Add a new Actor</CardHeader>
            <CardBody>
                <Form
                    onSubmit={e =>{
                        e.preventDefault();
                        handleFormSubmit({
                            name: actorInput.name,
                            age: actorInput.age,
                            gender: actorInput.gender,
                            movie: actorInput.movie
                        })
                    }}
                >
                    <FormGroup>
                        <Label for="actorName">Actor's Name'</Label>
                        <Input 
                            type="text"
                            name="actorName"
                            id="actorName"
                            value={actorInput.name}
                            onChange={e => updateFormFields("name", e.target.value)}
                        />
                        <FormText>Enter the name of the actor.</FormText>
                    </FormGroup>
                    <FormGroup>
                        <Label for="actorAge">Actor's age</Label>
                        <Input 
                            type="number"
                            name="actorAge"
                            id="actorAge"
                            value={actorInput.age}
                            onChange={e => updateFormFields("age", e.target.value)}
                        />
                        <FormText>Enter the age of the actor.</FormText>
                    </FormGroup>
                    <FormGroup>
                        <Label for="actorGender">Actor's gender</Label>
                        <Input 
                            type="text"
                            name="actorGender"
                            id="actorGender"
                            value={actorInput.gender}
                            onChange={e => updateFormFields("gender", e.target.value)}
                        />
                        <FormText>Enter the gender of the actor.</FormText>
                    </FormGroup>
                    <FormGroup>
                        <Label for="assignedMovie">Assigned to Movie</Label>
                        <Input 
                            type="number"
                            name="assignedMovie"
                            id="actorMovie"
                            value={actorInput.movie}
                           onChange={e => updateFormFields("movie", e.target.value)}
                        />
                        <FormText>Enter the title of the Movie assigned to the actor.</FormText>
                    </FormGroup>
                </Form>
            </CardBody>
            <CardFooter className="d-flex justify-content-between">
                <Button tag={RouterNavLink} to="/actors-details" color="warning">Cancel</Button>
                <Button 
                    color="primary" 
                    type="submit"
                    onClick={e => {
                        e.preventDefault();
                        handleFormSubmit((actor && actor.id) || null, {
                            name: actorInput.name,
                            age: actorInput.age,
                            gender: actorInput.gender,
                            movie: actorInput.movie
                        });
                    }}
                >Submit
                </Button>
            </CardFooter>
        </Card>
    )
};