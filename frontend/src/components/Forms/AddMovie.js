import React from 'react';
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
            <CardFooter>
                <Button className="btn btn-sm">Submit</Button>
            </CardFooter>
        </Card>
    )
};