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


export const AddMovieForm = (props) => {
    const url = `${API_URL}/movies`;
    const { editing, movie, token } = props.location.state;
    const [ movieInput, setMovieInput ] = useState({
        title: (editing && movie && movie.title) || "",
        release_date: (editing && movie && movie.release_date) || "",
        image_link:(editing && movie && movie.image_link) || "",
    });

    const updateFormFields = (field, value) => {
        setMovieInput({
            ...movieInput,
            [field]: value
        })
    };

    const handleFormSubmit = async (id, data) => {
        const result = await fetch(editing ? `${url}/${id}` : url, {
            method: editing ? "PATCH" : "POST",
            headers: {
                Authorization: "Bearer " + token,
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });
        const response = await result.json();

        setMovieInput({
            title: response.added_movie[0].title,
            release_date: response.added_movie[0].release_date,
            image_link: response.added_movie[0].image_link
        });
        props.history.push('/movies')

    };

    return (
        <Card inverse style={{ backgroundColor:'#333', borderColor:'#333'}}>
            <CardHeader className="text-primary">Add a new Movie</CardHeader>
            <CardBody>
                <Form
                    onSubmit={e => {
                        e.preventDefault();
                        handleFormSubmit({
                            title: movieInput.title,
                            release_date: movieInput.release_date,
                            image_link: movieInput.image_link
                        })
                    }}
                >
                    <FormGroup>
                        <Label for="movieTitle">Movie Title</Label>
                        <Input 
                            type="textarea" 
                            name="movieTitle" 
                            id="movieTitle" 
                            value={movieInput.title}
                            onChange={e => updateFormFields("title", e.target.value)}
                        />
                        <FormText>Enter the title of the movie.</FormText>
                    </FormGroup>
                    <FormGroup>
                        <Label for="imageLink">Cover Image Link</Label>
                        <Input 
                            type="textarea" 
                            name="imageLink" 
                            id="imageLink" 
                            value={movieInput.image_link}
                            onChange={e => updateFormFields("image_link", e.target.value)}
                        />
                        <FormText>Enter the image link address for the cover.</FormText>
                    </FormGroup>
                    <FormGroup>
                        <Label for="movieReleaseDate">Movie Release Date</Label>
                        <Input 
                            type="date" 
                            name="movieReleaseDate" 
                            id="movieReleaseDate"
                            value={movieInput.release_date}
                            onChange={e => updateFormFields("release_date", e.target.value)} 
                        />
                        <FormText>Enter the release date of the movie.</FormText>
                    </FormGroup>
                </Form>
            </CardBody>
            <CardFooter className="d-flex justify-content-between">
                <Button tag={RouterNavLink} to="/movies" color="warning">Cancel</Button>
                <Button 
                    color="primary" 
                    type="submit"
                    onClick={e => {
                        e.preventDefault();
                        handleFormSubmit((movie && movie.id) || null, {
                            title: movieInput.title,
                            release_date: movieInput.release_date,
                            image_link: movieInput.image_link
                        });

                    }}
                >Submit
                </Button>
            </CardFooter>
        </Card>
    )
};