%%%%
\version "2.22.0"

%% -----
%% Option 1:
%% Use a procedure to convert a number to pitch:
#(define (: r i)
   (apply
    ly:make-pitch
    (cons (1- (floor (/ i 12)))
          (list-ref `((0 0) (0 ,SHARP) (1 0) (1 ,SHARP)
                      (2 0) (3 0) (3 ,SHARP) (4 0)
                      (4 ,SHARP) (5 0) (5 ,SHARP) (6 0))
                    (modulo (+ r i) 12)))))


{
}

