import media
import fresh_tomatoes

memento = media.Movie('Memento',
							'A man juggles searching for his wife\'s murderer and keeping his short-term memory loss from being an obstacle.',
							'https://images-na.ssl-images-amazon.com/images/M/MV5BZTcyNjk1MjgtOWI3Mi00YzQwLWI5MTktMzY4ZmI2NDAyNzYzXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,681,1000_AL_.jpg',
							'https://www.youtube.com/watch?v=0vS0E9bBSL0')

forrest_gump  = media.Movie('Forrest Gump',
							'While not intelligent, Forrest Gump has accidentally been present at many historic moments, but his true love, Jenny Curran, eludes him.',
							'https://images-na.ssl-images-amazon.com/images/M/MV5BYThjM2MwZGMtMzg3Ny00NGRkLWE4M2EtYTBiNWMzOTY0YTI4XkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_SY1000_CR0,0,757,1000_AL_.jpg',
							'https://www.youtube.com/watch?v=bLvqoHBptjg')

inception = media.Movie('Inception',
							'A thief, who steals corporate secrets through use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO.',
							'https://images-na.ssl-images-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg',
							'https://www.youtube.com/watch?v=8hP9D6kZseM')

the_matrix = media.Movie('The Matrix',
							'A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.',
							'https://images-na.ssl-images-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,665,1000_AL_.jpg',
							'https://www.youtube.com/watch?v=m8e-FF8MsqU')

leon = media.Movie('Leon: The Professional',
							'Mathilda, a 12-year-old girl, is reluctantly taken in by Léon, a professional assassin, after her family is murdered. Léon and Mathilda form an unusual relationship, as she becomes his protégée and learns the assassin\'s trade.',
							'https://images-na.ssl-images-amazon.com/images/M/MV5BMjdjMGU3MGYtN2Y5ZC00MTE4LWE4YWQtMTBhMjc3MTk0ZDUwXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_SX664_AL_.jpg',
							'https://www.youtube.com/watch?v=ns4vh_xAn98')

interstellar = media.Movie('Interstellar',
							'A team of explorers travel through a wormhole in space in an attempt to ensure humanity\'s survival.',
							'https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_SY1000_CR0,0,640,1000_AL_.jpg',
							'https://www.youtube.com/watch?v=zSWdZVtXT7E')

movies = [memento, forrest_gump, inception, the_matrix, leon, interstellar]

fresh_tomatoes.open_movies_page(movies)