-- * PCCB 1-6-2
-- |

import Data.List

data ExtensionOf a = Finite a
                   | NegativeInfinity
                   | PositiveInfinity
                     deriving (Eq, Show)

instance Ord a => Ord (ExtensionOf a) where
    compare NegativeInfinity NegativeInfinity = EQ
    compare PositiveInfinity PositiveInfinity = EQ
    compare NegativeInfinity _                = LT
    compare PositiveInfinity _                = GT
    compare _                NegativeInfinity = GT
    compare _                PositiveInfinity = LT
    compare (Finite l)       (Finite r)       = compare l r


solve :: Int -> [Int] -> (Int, Int)
solve l as = solve' (NegativeInfinity::ExtensionOf Int, NegativeInfinity::ExtensionOf Int) l as
    where solve' acc@(Finite mx, Finite mn) l []      = (mx, mn)
          solve' acc@(       mx,        mn) l (a:as') = let mx' = max mx (Finite (max a (l - a)))
                                                            mn' = max mn (Finite (min a (l - a)))
                                                        in  solve' (mx', mn') l as'

getLength :: IO Int
getLength = do l <- getLine
               return (read l::Int)

getAnts :: IO [Int]
getAnts = do arg <- getLine
             return [(read a::Int) | a <- (words arg)]

--getAnts :: IO [(Int, Int)]
--getAnts = do arg <- getLine
--             return [((read l::Int), (read r::Int)) | (l:r:_) <- map (delimitWhen isDelimiter) (words arg)]

--delimitWhen :: (Char -> Bool) -> String -> [String]
--delimitWhen cnd s = case dropWhile cnd s of
--                  "" -> []
--                  s' -> w : delimitWhen cnd s''
--                        where (w, s'') = break cnd s'

--isDelimiter :: Char -> Bool
--isDelimiter c = case find (==c) delimiters of
--                  Just d  -> True
--                  Nothing -> False

--delimiters :: [Char]
--delimiters = ","

putAnsLn :: (Show a) => a -> IO ()
putAnsLn ans = putStrLn (show ans)

main = do l  <- getLength
          as <- getAnts
          putAnsLn (solve l as)
