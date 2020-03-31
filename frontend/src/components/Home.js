import React from "react";
import { Col, Row, Card, CardBody, CardText, CardImg, CardDeck } from "reactstrap";
import { Link } from "react-router-dom";
import { useAuth0 } from "../react-auth0-spa";
// import ActorsImg from '../assets/actors.jpg'
// import MoviesImg from '../assets/movies.jpg'

export const Home = () => {
  const { isAuthenticated } = useAuth0();
  return (
    <>
      {isAuthenticated ? (
        <CardDeck>
          <Card>
            <CardImg
              top
              width="100%"
              height="70%"
              src="https://image.shutterstock.com/image-photo/movie-clapper-film-reel-on-600w-169841813.jpg"
              alt="Movies img"
            />
            <CardBody>
              <Link to="/movies">Manage movies</Link>
            </CardBody>
          </Card>
          <Card>
            <CardImg
              top
              width="100%"
              height="70%"
              src="https://image.shutterstock.com/image-photo/medium-shot-actors-rehearsing-theater-600w-1270982080.jpg"
              alt="Actors img"
            />
            <CardBody>
              <Link to="/actors">Manage actors</Link>
            </CardBody>
          </Card>
        </CardDeck>
      ) : (
          <Card>
            <CardBody color="dark" className="homepage">
              <CardText>
              StephanGEL Casting Agency has less than a year of casting experience. This 
              platform models a company that is responsible for creating movies and managing 
              and assigning actors to those movies.
              </CardText>
              <CardText>
              As a casting assistant, you are authorized to see the details of the movies and the actors.
              </CardText>
              <CardText>
              You'll be authorized to create new actors as well as modifying movies if you are
              logged in as a Casting Director.
              </CardText>
              <CardText>
              Being an executive Producer, you have all the priviledges that a Casting Director has. 
              In addition, you can create and delete new movies.
              </CardText>
              <CardText>
              If you are new, kindly sign up/register for a new account by clicking on the loggin button.
              Wait for 2-3 days for your user account to be verified.  You can contact us upon creating your account.
              </CardText>
            </CardBody>
          </Card>
      )}
    </>
  );
};