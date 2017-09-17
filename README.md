#rex-sort

#Part 0

It's late at night. I was on the phone with my bud, talking about how he knew someone who worked on the 1995 sci-comedy cinematic adventure Theodore Rex. It was then, much like JK Rowling's fated train ride, I also had a thought simply pop into my head. A thought that would become my magnum opus.

I had the idea to sort the entire film, frame by frame, by average brightness. What this project lacks in Quidditch, though, it makes up in animatronic dinosaurs. I may or may not have found a torrent and got to work.

#Part 1

My first plan was to forget about the movie's audio, generate an image sequence, and stitch that together with ffmpeg. As much as I'd like to try and use movie-editing libraries, they'd probably be unbearably slow and as a Python beginner OpenCV already has pretty good documentation, an active community, and (arguably most importantly) lots of StackOverflow banter. I can also figure out how to stitch the audio in later.

I started tests for this project on my trusty 2012 MacBook Pro, but as soon as I realized that further work would 100% set the machine ablaze I moved to my Windows desktop where the i7 worked nearly twice as fast *and* didn't try to melt itself down. This was one of my first run-ins with the real-world limitations of hardware speed - in school and most of my web projects, nothing had scaled enough to take more than a few seconds or even a minute. That's not the case when you're dealing with a feature film.

Generating the image sequence was pretty quick to program, but not quick to run. OpenCV made reading the frames quick, and Numpy made the summation of the frame's pixels a one-line operation. I chose to embed the brightness level and then the frame number so as to avoid any naming collisions.

I exported the frame image sequence onto an extra hard drive because, uh, I just didn't have 60GB of free SSD space for png files of Whoopi Goldberg. 43:23.042000 minutes later and I was the proud owner of 131925 individual images named after the sum of their pixels and a CSV file detailing the same information.
