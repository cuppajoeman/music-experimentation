



## Game loop
running = True
while running:

    #1 Process input/events
    clock.tick(FPS)     ## will make the loop run at the same speed all the time
    for event in pygame.event.get():        # gets all the events which have occured till now and keeps tab of them.
        ## listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False


    #2 Update
    all_sprites.update()


    #3 Draw/render
    #screen.fill(pygame.color.THECOLORS['black'])

    all_sprites.draw(screen)
    ########################


    # About to start drawing the squares with the numbers inside of them 
    # Making a new toolbox entry that draws text at poisition while also being centered.


        



    ########################

    ## Done after drawing everything to the screen
    pygame.display.flip()       

pygame.quit()
