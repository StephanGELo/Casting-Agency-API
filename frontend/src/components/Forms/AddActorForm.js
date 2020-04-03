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

    return (
        <Card inverse style={{ backgroundColor:'#333', borderColor:'#333'}}>
            <CardHeader>Add a new Actor</CardHeader>
            <CardBody>

            </CardBody>
            <CardFooter className="d-flex justify-content-between">
                <Button tag={RouterNavLink} to="/actors-details" color="warning">Cancel</Button>
                <Button 
                    color="primary" 
                    type="submit"
                >Submit
                </Button>
            </CardFooter>
        </Card>
    )
};