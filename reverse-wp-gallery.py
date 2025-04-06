""""
reverse the order of images in a gallery
2025-04-06 Mirko Javurek

switch to code view in edit post/page mode
cut gallery image code between
   <!-- wp:gallery {"linkTo":"file"} --><figure class="wp-block-gallery has-nested-images columns-default is-cropped">
and
   </figure><!-- /wp:gallery -->
into a text-file named wp-gallery.html
the code for each image must be 4 lines long - add newline(s) after the last image if required, like (line 4 is empty!):
   <!-- wp:image {"id":926,"sizeSlug":"large","linkDestination":"media"} -->
   <figure class="wp-block-image size-large"><a href="https://gegenton.wordpress.com/wp-content/uploads/2025/03/20250329_204616-1.jpg"><img src="https://gegenton.wordpress.com/wp-content/uploads/2025/03/20250329_204616-1.jpg?w=1024" alt="" class="wp-image-926" /></a></figure>
   <!-- /wp:image -->

paste the result of this output back in the code
""""
with open("wp-gallery.html") as f:
   lines = [line.rstrip() for line in f]
n = len(lines)
for i in range(n-4, -1, -4):
    for j in range(i,i+4):
        print(lines[j])

