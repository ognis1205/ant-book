-- * PCCB 1-6-1
-- |

import Data.List

solve :: [Int] -> Bool
solve [] = False
solve es = case find (inequality) (combinations 3 es) of
             Nothing  -> False
             Just cmb -> True

inequality :: [Int] -> Bool
inequality []        = False
inequality es@(x:xs) = let es'@(m:xs') = reverse (sort es)
                       in  if m > foldl (+) 0 xs'
                           then True
                           else False

combinations :: Int -> [a] ->[[a]]
combinations n xs = let l = length xs
                    in  if n > l
                        then []
                        else combinations' xs !! (l - n)
                            where combinations' []     = [[[]]]
                                  combinations' (x:xs) = let next = combinations' xs
                                                         in  zipWith (++) ([]:next) (map (map (x:)) next ++ [[]])

parse :: IO [Int]
parse = do ns <- getLine
           return [(read n::Int) | n <- (words ns)]

putAnsLn :: (Show a) => a -> IO ()
putAnsLn ans = putStrLn (show ans)

main = do es <- parse
          putAnsLn (solve es)
