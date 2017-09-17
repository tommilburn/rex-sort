# rex-sort

## Part 0

It's late at night. I was on the phone with my bud, talking about how he knew someone who worked on the [1995 buddy-cop sci-fi-comedy cinematic adventure Theodore Rex](https://www.youtube.com/watch?v=dY7gsUL9Xkk). It was then, much like JK Rowling's fated train ride, I also had a thought simply pop into my head. A thought that would become my magnum opus. My greatest work. My destiny.

I had the idea to sort the entire film, frame by frame, by average brightness. What this project lacks in weasleys, though, it makes up in animatronic dinosaurs. I may or may not have found a torrent and got to work.

Setting up OpenCV with Python and ffmpeg was the longest and most frustrating part of this project. Installing OpenCV meant updating brew, and updating brew required fixing all of the weird half-installed packages and broken taps left over from years of neglect and a long time of not really understanding package managers when I was in school. Setting it up on Windows was pretty easy,

## Part 1

My first plan was to forget about the movie's audio, generate an image sequence, and stitch that together with ffmpeg. As much as I'd like to try and use movie-editing libraries, they'd probably be unbearably slow and as a Python beginner OpenCV already has pretty good documentation, an active community, and (arguably most importantly) lots of StackOverflow banter. I can also figure out how to stitch the audio in later.

I started tests for this project on my trusty 2012 MacBook Pro, but as soon as I realized that further work would 100% set the machine ablaze I moved to my Windows desktop where the i7 worked nearly twice as fast *and* didn't try to self-immolate in protest. This was one of my first run-ins with the ~real~-world limitations of hardware speed - in school and most of my web projects, nothing had scaled enough to take more than a few seconds or even a minute. That's not the case when you're dealing with a 131,925 frame feature-film.

Analyzing the frame information and saving each frame individually with that information was quick to program, but not quick to run. OpenCV made reading the frames quick, and Numpy made the summation of the frame's pixels a one-line operation. I chose to create PNGs named [brightness level] [frame number].png so I could still sort it easily but avoid collisions if two frames had the same brightness level.

I exported the frame image sequence onto an extra hard drive because, uh, I just didn't have 60GB of free SSD space for png files of Whoopi Goldberg. 43:23.042000 minutes later and I was the proud owner of 131K images and a CSV file for quick reference to all of the generated data.

Another 2:22.425000 and the files are all renamed from 000001 to 131925. Then came stitching them together, and with that learning how ffmpeg works. It took a few minutes of fumbling around with codec settings and getting the output video file to be a high enough quality, but after two or three hours of testing I found the

`ffmpeg -i %06d.png -vcodec libx264 -r 25 -b:v 6000k video.avi`

command did what I needed. Now I had a video, but no sound.

## Part 2: Sound

This turned out to be super quick - the [built-in python wav module](https://docs.python.org/2/library/wave.html) does exactly what I needed it to do - read from the CSV file with the frame information, scrub to that frame's location in the seperate audio WAV file I had pulled out of the avi (because the torrent I may or may not have downloaded may or may not have had Russian audio as the primary audio track), and write one frame's worth of audio to an output buffer. 1:05.582000 minutes later, and it worked like a charm. The actual code is only ~30 lines. Curiously, the first few thousand frames run nearly instantaneously, and the last 30% of the movie takes up almost the entire runtime. Will research and report back.

One more 1:27:57.00-minute long pass through ffmpeg to stitch the audio and video together, and we're done.

## Part 3

[Here it is!](https://youtu.be/VyY3ZXAaMeQ)

If my math is correct, all this can be done in under an hour if you have ~80GB of space free and a computer with nothing to do.

I don't recommend it.
