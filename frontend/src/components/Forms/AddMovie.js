import React from 'react';
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

export const AddMovie = () => {
    return (
        <Card inverse style={{ backgroundColor:'#333', borderColor:'#333'}}>
            <CardHeader>Add a new Movie</CardHeader>
            <CardBody>
                <Form>
                    <FormGroup>
                        <Label for="movieTitle">Movie Title</Label>
                        <Input type="textarea" name="movieTitle" id="movieTitle" />
                        <FormText>Enter the title of the movie.</FormText>
                    </FormGroup>
                    <FormGroup>
                        <Label for="movieReleaseDate">Movie Release Date</Label>
                        <Input type="date" name="movieReleaseDate" id="movieReleaseDate" />
                        <FormText>Enter the release date of the movie.</FormText>
                    </FormGroup>
                </Form>
            </CardBody>
            <CardFooter className="d-flex justify-content-between">
                <Button tag={RouterNavLink} to="/movies" color="warning">Cancel</Button>
                <Button color="primary" type="submit">Submit</Button>
            </CardFooter>
        </Card>
    )
};