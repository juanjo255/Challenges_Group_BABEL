class trim:

    def __init__(self, fastq) -> None:
        self.fastq = open (fastq).readlines ()
        
    def window (self, window_size, quality) -> None:

        # parse the document and take quality 
        for i in range (0, len (self.fastq), 4):

            sec_quality = self.fastq [i+3].strip ()
            window_phre_score = list (map (lambda letter: ord (letter)-33 , sec_quality [:window_size]))

            # we advance in the sec_quiality
            for ascii in range (5, len (sec_quality)):
                del window_phre_score [0]
                window_phre_score.append (ord (sec_quality [ascii])-33)
                print ( sum (window_phre_score) /window_size)

            # assess only the first sequence of the document
            break


trim ("test_sanger.fastq").window (5, 20)