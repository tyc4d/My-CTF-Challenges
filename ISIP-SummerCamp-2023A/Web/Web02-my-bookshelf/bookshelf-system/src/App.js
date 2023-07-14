import React, { useEffect, useState } from 'react';
import axios from 'axios';
import {
  Container,
  Typography,
  TextField,
  Button,
  Grid,
  Card,
  CardContent,
  CardMedia,
  makeStyles
} from '@mui/material';

const useStyles = makeStyles((theme) => ({
  // Your existing styles...
}));

const App = () => {
  const classes = useStyles();
  const [books, setBooks] = useState([]);
  const [title, setTitle] = useState('');
  const [author, setAuthor] = useState('');
  const [coverImage, setCoverImage] = useState('');

  const fetchBooks = async () => {
    const response = await axios.get('http://127.0.0.1:5000/api/books');
    setBooks(response.data);
  };

  const addBook = async () => {
    await axios.post('http://127.0.0.1:5000/api/books', { title, author, cover_image: coverImage });
    setTitle('');
    setAuthor('');
    setCoverImage('');
    fetchBooks();
  };

  useEffect(() => {
    fetchBooks();
  }, []);

  return (
    <Container maxWidth="md" className={classes.root}>
      <Typography variant="h4" component="h1" align="center" gutterBottom>
        Bookshelf System
      </Typography>
      <Grid container justifyContent="center">
        <Grid item xs={12} md={6} className={classes.form}>
          <TextField
            label="Title"
            fullWidth
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            className={classes.inputField}
          />
          <TextField
            label="Author"
            fullWidth
            value={author}
            onChange={(e) => setAuthor(e.target.value)}
            className={classes.inputField}
          />
          <TextField
            label="Cover Image URL"
            fullWidth
            value={coverImage}
            onChange={(e) => setCoverImage(e.target.value)}
            className={classes.inputField}
          />
          <Button variant="contained" onClick={addBook}>
            Add Book
          </Button>
        </Grid>
      </Grid>
      <Grid container spacing={2} className={classes.cardContainer}>
        {books.map((book) => (
          <Grid item xs={12} sm={6} md={4} key={book.id}>
            <Card elevation={3}>
              <CardMedia
                component="img"
                className={classes.cardMedia}
                image={book.cover_image}
                alt={book.title}
              />
              <CardContent>
                <Typography variant="h6" gutterBottom>
                  {book.title}
                </Typography>
                <Typography variant="subtitle1" color="textSecondary">
                  {book.author}
                </Typography>
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>
    </Container>
  );
};

export default App;